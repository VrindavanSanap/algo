#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool validate_ipv4(char *ipv4) { 

  // conds
  // 4 ints (0-255) seperated by '.'
  // no leading zeros
  
  return true; 


}
bool validate_ipv6(char *ipv4) { return true; }

char *validate_ip(char *ip_addr) {
  for (int i = 0; i < strlen(ip_addr); i++) {
    if (ip_addr[i] == '.') {
      if (validate_ipv4(ip_addr)) {
        return "ipv4";
      }

    } else if (ip_addr[i] == ':') {
      if (validate_ipv6(ip_addr)) {
        return "ipv6";
      }
    }
  }
  return "Neither";
}

int main() {
  char *a1 = "172.16.254.1";
  char *a2 = "2001:0db8:85a3:0:0:8A2E:0370:7334";

  printf("%s",validate_ip(a1));
  printf("%s", validate_ip(a2));
}
