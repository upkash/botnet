malware: bot.o client.o main.o
	g++ -o malware bot.o client.o main.o -lcurl
bot.o: bot.cpp bot.h
	g++ -c -Wall bot.cpp
client.o: client.cpp client.h
	g++ -c -Wall client.cpp -lcurl
main.o:
	g++ -c -Wall main.cpp
clean:
	rm -f malware client.o bot.o main.o