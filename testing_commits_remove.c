#include <stdio.h>
#include <stdlib.h>

int main() {
    system("rm random.txt");
    system("git add .");
    system("git commit -m \"removed random.txt file\"");
    system("git push -u origin master");

    return 0;
}