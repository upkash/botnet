#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <netdb.h> 


//slave node formulate request for the master given endpoint, req type, and data(json) for post
char* create_request(char* type, char* endpoint, char* data){
    char* request = (char*)malloc(1000);
    strcat(request, type);
    strcat(request, " ");
    strcat(request, endpoint);
    strcat(request, " HTTP/1.1\r\n");
    strcat(request, "Host: 10.0.0.14:3000\r\n");

    strcat(request, "Accept: */*\r\n");
    strcat(request, "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36\r\n");
    strcat(request, "Content-Type: application/json\r\n");
    strcat(request, data);
    strcat(request, "\0");
    return request;

}

char* form_ping_json(){
    char* data = (char*)malloc(400);
    strcat(data, "{ \"platform\": ");
    strcat(data, "endlmfao,");
    strcat(data, " \"hostname\": ");
    strcat(data, "behenchod,");
    strcat(data, " \"username\": ");
    strcat(data, "fiveoh }");
    return data;
}

char* send_request(char* request, char* type){
    int port = 80;
    char* home_addr = "10.0.0.14";
    struct sockaddr_in serv_addr;

    int sockfd, bytes, sent, received, total;

    char message[1024], response[4096];
    strcpy(message, request);
    printf(message);
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
    printf(request);
    total = 1000;
    printf("hanging after total\n");
    printf(total);
    sent = 0;
    do {
        bytes = write(sockfd,request+sent,total-sent);
        if (bytes < 0)
            printf("ERROR writing message to socket");
        if (bytes == 0)
            break;
        sent+=bytes;
    } while (sent < total);

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

    return 0;

}


int main(int argc, char** argv){
    char* data = form_ping_json();
    printf("first malloc chillen\n");
    //printf("%s", data);
    char* req = create_request("POST", "/api/6669/status","sdfsf");
    char* r = send_request(req, "POST");
	printf("second malloc chillen\n");
} 
