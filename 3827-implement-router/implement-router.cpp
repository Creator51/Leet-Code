#include <bits/stdc++.h>
using namespace std;

class Router {
public:
    Router(int memoryLimit) : memoryLimit(memoryLimit) {}

    bool addPacket(int source, int destination, int timestamp) {
        tuple<int,int,int> key = {source, destination, timestamp};
        if (seen.count(key)) return false;

        if ((int)q.size() == memoryLimit) {
            forwardPacket(); // evict oldest if full
        }

        q.push(key);
        seen.insert(key);
        dest2timestamps[destination].push_back(timestamp);
        return true;
    }

    vector<int> forwardPacket() {
        if (q.empty()) return {};

        auto [src, dst, ts] = q.front();
        q.pop();
        seen.erase({src, dst, ts});
        dest2forwardedCount[dst]++;

        return {src, dst, ts};
    }

    int getCount(int destination, int startTime, int endTime) {
        if (!dest2timestamps.count(destination)) return 0;

        const auto& arr = dest2timestamps[destination];
        int startIndex = dest2forwardedCount[destination];

        if (startIndex >= (int)arr.size()) return 0;

        auto lo = lower_bound(arr.begin() + startIndex, arr.end(), startTime);
        auto hi = upper_bound(arr.begin() + startIndex, arr.end(), endTime);
        return hi - lo;
    }

private:
    int memoryLimit;
    queue<tuple<int,int,int>> q;   // FIFO packets
    unordered_set<tuple<int,int,int>, 
        function<size_t(const tuple<int,int,int>&)>> seen{
        0, [](const tuple<int,int,int>& t){
            auto [a,b,c] = t;
            return ((a*1315423911u + b*2654435761u) ^ c);
        }
    };

    unordered_map<int, vector<int>> dest2timestamps;   // dest -> timestamps
    unordered_map<int, int> dest2forwardedCount;       // dest -> count of forwarded
};