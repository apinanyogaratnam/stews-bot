#include <stdio.h>
#include <stdlib.h>

int main() {
    system("touch random.txt");
    system("git add .");
    system("git commit -m \"added random.txt file\"");
    system("git push -u origin master");

    return 0;
}