/*program in C to Check Whether a Number can be Express as Sum of Two Prime Numbers*/
#include<stdio.h>

int main()
{
	int n,i,fact,j,f=0,temp,k=0,array[100];
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    for(i=1; i<=n; i++)
    {
        fact=0;
        for(j=1; j<=n; j++)
        {
            if(i%j==0)
                fact++;
        }
        if(fact==2){
            array[k]=i;
                        k++;}
    }
        for(int i=0;i<k-1;i++){
            for(int j=i+1;j<k;j++){
                if(array[i]<array[j]){
                    temp=array[j];
                    array[j]=array[i];
                    array[i]=temp;
                }
            }
        }
        for(int i=0;i<k-1;i++){
            for(int j=i;j<k;j++){
                if(array[i]+array[j]==n){
                    printf("%d = %d + %d\n",n,array[j],array[i]);
                    break;
                }
            }
        }

	return 0;
}
