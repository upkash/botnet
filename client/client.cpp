#include <stdio.h>
#include <curl/curl.h>
#include <string>
#include <iostream>
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <arpa/inet.h>
#include <netdb.h> 
#include "client.h"

//slave node formulate request for the master given endpoint, req type, and data(json) for post

static size_t WriteCallBack(void *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

char* send_post(string data, string endpoint){
    // CURL *curl;
    // CURLcode res;
    // string readBuffer;
    // curl = curl_easy_init();
    // if(curl){
    //     struct curl_slist *headers = NULL;
    //     headers = curl_slist_append(headers, "Accept: application/json");
    //     headers = curl_slist_append(headers, "Content-Type: application/json");
    //     headers = curl_slist_append(headers, "charset: utf-8"); 
    //     curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    //     curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    //     curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallBack);
    //     curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());
    //     curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
    //     res = curl_easy_perform(curl);
    //     curl_easy_cleanup(curl);

    //     return readBuffer;
    // }
    
    string raw = string("POST ") + endpoint + string(" HTTP/1.1\r\n");
    raw += "Host: 10.0.0.14:3000\r\n";
    raw +=  "Accept: */*\r\n";
    raw += "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36\r\n";
    raw += "Content-Type: application/json\r\n";
    raw += data;
    
    int request_len = raw.length()+1;
    cout << request_len << endl;
    char* request = (char*)malloc(request_len);
    strcpy(request, raw.c_str());
    strcat(request, "\0");
    
    
    int port = 80;
    char* home_addr = "10.0.0.14";
    struct sockaddr_in serv_addr;

    int sockfd, bytes, sent, received, total;

    char response[4096];
    printf("hanging\n");
    printf("catch\n");
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0){
        printf("checking sockfd\n");
        exit(1);
    }
    
    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    serv_addr.sin_addr.s_addr = inet_addr("10.0.0.14");
    printf("end?\n");
    //printf(inet_addr(&home_addr));
    
    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0)
        printf("ERROR connecting");
    printf("hanging4\n");
   
    total = request_len;
    printf("hanging after total\n");
    send(sockfd, request, request_len, 0);
    // sent = 0;
    // int write_count = 0;
    // do {
    //     printf("enml\n");
    //     bytes = write(sockfd,request+sent,total-sent);
    //     printf("write\n");
    //     if (bytes < 0)
    //         printf("ERROR writing message to socket");
    //     if (bytes == 0)
    //         break;
    //     printf("%d", bytes);
    //     printf("\n");
    //     sent = sent + bytes;
    //     printf("%d",sent);
    // } while (sent < total);

    /* receive the response */
    memset(response,0,sizeof(response));
    total = sizeof(response)-1;
    received = 0;
    do {
        bytes = read(sockfd,response+received,total-received);
        if (bytes < 0)
            printf("ERROR reading response from socket");
        if (bytes == 0)
            break;
        received+=bytes;
    } while (received < total);

    if (received == total)
        printf("ERROR storing complete response from socket");

    /* close the socket */
    close(sockfd);

    /* process response */
    printf("Response:\n%s\n",response);

}


