///week12-2.cpp
#include <stdio.h>
int main()
{
    int n = 2;
    int a[2][2] = { {10,20}, {11,22} };
    int b[2][2] = { {2,1}, {3,2} };
    int c[2][2];
    ///Part 1 �|Ū a[i][j]�C���]�n,�N���ΦAŪ
    ///Part 2 �|Ū b[i][j]�C���]�n,�N���ΦAŪ
    for(int i=0; i<n; i++){ ///Part 3 �L���
        for(int j=0; j<n; j++){
            int * p1 = & a[i][j]; ///���F�b Tutor �q�b�Y
            printf("%3d ", a[i][j] );
        }
        printf("\n");
    }
}
