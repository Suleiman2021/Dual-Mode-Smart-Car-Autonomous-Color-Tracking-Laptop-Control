/*
  WiFiAccessPoint.ino creates a WiFi access point and provides a web server on it.

  Steps:
  1. Connect to the access point "yourAp"
  2. Point your web browser to http://192.168.4.1/H to turn the LED on or http://192.168.4.1/L to turn it off
     OR
     Run raw TCP "GET /H" and "GET /L" on PuTTY terminal with 192.168.4.1 as IP address and 80 as port

  Created for arduino-esp32 on 04 July, 2018
  by Elochukwu Ifediora (fedy0)
*/

#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

int echoPin = 22; 
int trigPin = 23; 

long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

// Set these to your desired credentials.
const char *ssid = "esp32";
const char *password = "12344321";

WiFiServer server(80);


void setup() {

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT

  pinMode(15,OUTPUT);//1
  pinMode(16,OUTPUT);//1
  pinMode(13,OUTPUT);//2
  pinMode(12,OUTPUT);//2

  Serial.begin(115200);
  Serial.println();
  
  
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  WiFi.softAP(ssid, password);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");
}


void right(){
   
    digitalWrite(15,HIGH);
    digitalWrite(16,LOW);
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
    
  }
  void forward(){
  
     digitalWrite(15,LOW);
    digitalWrite(16,HIGH);
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
    
  }
  void backward(){
   
     digitalWrite(15,HIGH);
    digitalWrite(16,LOW);
    digitalWrite(13,LOW);
    digitalWrite(12,HIGH);
   
  }
  void left(){
   
  digitalWrite(15,LOW);
    digitalWrite(16,HIGH);
    digitalWrite(13,LOW);
    digitalWrite(12,HIGH);
   
  }
  void stop_p(){
   
  digitalWrite(15,LOW);
    digitalWrite(16,LOW);
    digitalWrite(13,LOW);
    digitalWrite(12,LOW);
   
  }
  

void loop() {

digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
        
  
  WiFiClient client = server.available();   // listen for incoming clients

  

  if (client) {                             // if you get a client,
    Serial.println("New Client.");           // print a message out the serial port
                   
      // Clears the trigPin condition
  

    Serial.print("Client connected with IP:");
    Serial.println(client.remoteIP());
    char c = client.read();             // read a byte, then
    Serial.println(c);
    if(distance <= 10 ){
      stop_p();
      }
    else{
    if(c == 'R'){
      right();
      delay(510);
      forward();
      }
    
    else if(c == 'L'){
      left();
      delay(510);
      forward();
      }
    
    else if(c == 'U'){
      forward();
      }
     
    else if(c == 'B'){
      backward();
      delay(510);
      stop_p();
      }
   
      }
      //---------------------------------------------------------------------

      if(c == 'u'){
      forward();
      }
    else if(c == 'b'){
      backward();
      }
    else if(c == 'r'){
      right();
      }

    else if(c == 'l'){
      left();
      }
    else if(c == 's'){
      stop_p();
      }
        
     
    
    
    
    
    
    // close the connection:
    
    client.stop();
    Serial.println("Client Disconnected.");
  }
}
