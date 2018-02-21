#include<stdio.h>
#include<conio.h>
void main()
{
char a[3][3],z[10];
int x=0,y=0,i;
int n=0,e=1,s=2,w=3;
int dir=n;
a[x][y]='O';
clrscr();
printf("\n**************ROBOT GAME***************");
printf("\nsize of the box is 3*3");
printf("\nenter the values to move and rotate(m and r)");
for(i=0;i<=10;i++)
{
  scanf("%d",&z[i]);
  if(z[i]==' ')
   break;
  else if(z[i]=='r'&& z[i]=='R')
  {


    dir=dir+1;
    if(dir==4)
    dir=0;

  }
  else if(z[i]=='m'&& z[i]=='M')
  {

   if((dir==n)&&(x-1!=-1))
     x=x-1;
   else if((dir==e)&&(x+1<3))
     x=x+1;
   else if((dir==w)&&(y-1!=-1))
     y=y-1;
   else if((dir==s)&&(y+1<3))
     y=y+1;
   else
     continue;
   printf("\nThe position of the robot is %d%d",&x,&y);

  }


  else
  {
  printf("\nenter either 'm' or 'r'");

  }
}

/*int direction()
{
  int dir;
  dir=dir+1;
  if(dir==4)
    dir=0;
   return dir;
}               void move()
{
   if((dir==n)&&(x-1!=-1))
     x=x-1;
   else if((dir==e)&&(x+1<3))
     x=x+1;
   else if((dir==w)&&(y-1!=-1))
     y=y-1;
   else if((dir==s)&&(y+1<3))
     y=y+1;
   else
   break;
   printf("The position of the robot is %d%d",&x,&y);

} */
switch(dir)
{
    case 0:
	   printf("\nThe robo is facing towards NORTH");
	   break;
    case 1:
	   printf("\nThe robo is facing towards EAST");
	   break;
    case 2:
	  printf("\nThe robo is facing towards SOUTH");
	   break;
    case 3:
	   printf("\nThe robo is facing towards WEST");
	   break;
    default:
	    break;
}


  getch();
}