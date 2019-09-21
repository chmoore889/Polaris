
#include <wiringPi.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define BUTTON_PIN 25

int main()
{
	wiringPiSetup();
	pinMode(BUTTON_PIN,INPUT);
	pullUpDnControl(BUTTON_PIN,PUD_DOWN);

//	pinMode(29,OUTPUT);

	uint8_t buttonState;

	for(;;)
	{
		buttonState = digitalRead(BUTTON_PIN);
//		printf("%d\n",buttonState);

		if(buttonState == 1)
		{
			printf("Button Pressed\n");

			//Audio recording
			system("nohup sudo arecord -D plughw:1,0 -f cd -d 7 result.wav &");
			system("ffmpeg -i result.wav -ac 1 mono_result.wav");		
//			digitalWrite(29,HIGH);

			int error = system("python startup.py");
			if(error == -1)
			{
				printf("Error on python script startup");
				exit(-1);
			}
		}
		else
		{
			printf("Button Unpressed\n");
//			digitalWrite(29,LOW);
		}
		fflush(stdout);
	}
	return 0;
}
