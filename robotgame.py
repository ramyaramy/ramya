/*robot will move and route acccording to value*/

#include <stdio.h>
#include <conio.h>
void main()
{
    char z[20];
    int count=0;
    int x=0,y=0;
    int dir=0;
    printf("\n************ROBOT************");
    printf("\nThe matrix has 3*3 boxes");
    printf("\nEnter the either m or r\n");
    scanf("%s",z);
    for(int i = 0;z[i]!='\0';i++)
    {
         count=count+1;
    }
    for(int i=0;i<count;i++)
    {
       if((z[i]=='m')||(z[i]=='M'))
        {
         if((dir==0)&&((x-1)!=-1))
           x=x-1;
         if((dir==1)&&((y+1)<3))
           y=y+1;
         if((dir==2)&&((x+1)<3))
           x=x+1;
         if((dir==3)&&((y-1)!=-1))
           y=y-1;
         
        }  
    
        if((z[i]=='r')||(z[i]=='R'))
        {
            dir=dir+1;
          if(dir==4)
             dir=0;
        }
        if(((z[i]!='r')&&(z[i]!='R'))&&((z[i]!='m')&&(z[i]!='M')))
        printf("\ninvalid input %c",z[i]);
    }
    if(dir==0)
        printf("\nThe robot is in north");
    if(dir==1)
        printf("\nThe robot is in east");
    if(dir==2)
        printf("\nThe robot is in south");
    if(dir==3)
        printf("\nThe robot is in west");
        printf("\nThe position of the robot is %d,%d",x,y);
    getch();
}
