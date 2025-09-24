class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        string result="";

        if((long long)numerator * (long long)denominator < 0){
            result+='-';
        }

        long long absNumerator=labs(numerator);
        long long absDenominator=labs(denominator);

        long long division=absNumerator/absDenominator;

        result+=to_string(division);
        long long remainder=absNumerator%absDenominator;
        if(remainder==0)
        return result;

        result+='.';
        unordered_map<int,int> mp;

        while(remainder!=0){
            if(mp.count(remainder)){
                result.insert(mp[remainder],"(");
                result+=")";
                return result;
            }

            mp[remainder]=result.length();

            remainder*=10;
            int digit=remainder/absDenominator;
            result+=to_string(digit);

            remainder=remainder%absDenominator;
        } 

    return result;
       
    }
};
