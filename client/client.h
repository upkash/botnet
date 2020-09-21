#ifndef CLIENT_H
#define CLIENT_H

#include <stdio.h>
using namespace std;
static size_t WriteCallBack(void *contents, size_t size, size_t nmemb, void *userp);
string send_get(string url);
string send_post(string data, string url);

#endif