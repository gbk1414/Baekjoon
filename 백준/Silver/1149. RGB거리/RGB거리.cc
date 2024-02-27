#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#include <algorithm>
using namespace std;

int N;
int cost[1000][3];
int ans;

void coloring() {
	for (int i = 1; i < N; i++) {
		cost[i][1] += min(cost[i - 1][2], cost[i - 1][0]);
		cost[i][2] += min(cost[i - 1][1], cost[i - 1][0]);
		cost[i][0] += min(cost[i - 1][2], cost[i - 1][1]);
	}
	ans = min(cost[N - 1][1], cost[N - 1][2]);
	ans = min(ans, cost[N - 1][0]);
}

int main() {
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%d", &cost[i][j]);
		}
	}
	coloring();
	printf("%d", ans);
}