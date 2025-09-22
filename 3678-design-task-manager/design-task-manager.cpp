class TaskManager {
public:
    typedef pair<int,int> p;
    priority_queue<p> maxHeap;//prioriy ,task ID
    unordered_map<int,int> taskpriority; // task->priority
    unordered_map<int,int> taskowner; //task-> userId

    TaskManager(vector<vector<int>>& tasks) {
        for( auto &task : tasks){
            add(task[0],task[1],task[2]);
        }
        
    }
    
    void add(int userId, int taskId, int priority) {
        maxHeap.push({priority,taskId});
        taskpriority[taskId]=priority;
        taskowner[taskId]=userId;
    }
    
    void edit(int taskId, int newPriority) {
        maxHeap.push({newPriority,taskId});
        taskpriority[taskId]=newPriority;
        
    }
    
    void rmv(int taskId) {
        taskpriority[taskId]=-1;
        
    }
    
    int execTop() {
        while(!maxHeap.empty()){
            auto [prio,taskid]=maxHeap.top();
            maxHeap.pop();

            if(prio==taskpriority[taskid]){ //Fresh Not stale
            taskpriority[taskid]=-1;
            return taskowner[taskid];
            }
        }
        return -1;
        
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */