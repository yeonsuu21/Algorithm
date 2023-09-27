#include <stdio.h>
#include <ctype.h> 
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    int i=0;
    scanf("%s", s1);
 while (s1[i])
    {
    	// 소문자를 판별하여
        if (isupper(s1[i]))
        {
        	//소문자를 대문자로
            s1[i] = tolower(s1[i]);
        }
        // 대문자를 판별하여
        else if (islower(s1[i]))
        {
        	//대문자를 소문자로
            s1[i] = toupper(s1[i]);
        }
        // 문자열 수만큼 증가하여 위 수식을 반복
        i++;
    }
 printf(s1);
    return 0;
}
