class Solution {
public:
    int reverse(int x) {
        
        string sX = to_string(x);
        bool neg = false;
        int l = sX.length();
        if (sX[0] == '-') {
            neg = true;
            l--;
            sX = sX.substr(1, l);
        }
/*        string inverse;
        for (int i = 0; i < l; i++) {
            cout << sX[l-i-1] << endl;
            inverse[i] = sX[l-i-1];
        }*/
        int result = 0;
        for (int i = 0; i < l; i++) {
            // cout << sX[i] - '0';
            // cout << pow(10, i)<< endl;
            result += (pow(10, i)) * (sX[i] - '0'); 
        }
        if (result == pow(2, 31) * -1) {
            return 0;
        }
        if (neg != false) {
            result = result * -1;
        } 
        if (result == pow(2, 31) || result == pow(2, 31) * -1) {
            return 0;
        } else {
            return result;
        }
    }
};
