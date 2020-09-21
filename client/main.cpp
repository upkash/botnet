#include <stdio.h>
#include <string>
#include <iostream>
#include <chrono>
#include <thread>
#include "bot.h"
#include "client.h"
using namespace std;
int main(){
    Bot bot = Bot("windows", "1236", "behen", "choot", "10.0.0.14");
    cout << bot.ping_server() << endl;
    while(true){
        bot.ping_server();
        cout << "iteration" << endl;
        this_thread::sleep_for(chrono::seconds(1)); 
    }


    return 0;
}