#include <iostream>
#include <string>
using namespace std;
int main() {
    string x = "\\yoyoyo";
    string ms_and ,ms_xor,ms_or;
    for(char c : x){
        ms_and += c & 127;
        ms_xor += c ^ 127;
        ms_or += c |  127;
    }
    cout<<"ori: "<< x << endl;
    cout<<"and modified: "<< ms_and<<endl;
    cout<<"xor modified: "<< ms_xor<<endl;
    cout<<"or modified: "<< ms_or<<endl;
    return 0;
}

// class Prac1{
// static int XorAscii(String str, int len)
// {

// 	int ans = 0;

// 	for (int i = 0; i < len; i++) {

// 		ans = (127 ^ ((str.charAt(i))));
// 	}
// 	return ans;
// }

// public static void main(String[] args)
// {

// 	String str = "H";
// 	int len = str.length();
// 	System.out.print(" XOR of given is : " +XorAscii(str, len) +"\n");


// }
// }



