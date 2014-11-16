#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <time.h> 

using namespace::std;

int getSortedness(const vector<int> & s)
{
	int r = 0;
	for (int j = s.size() - 1; j >= 0; j--) {
		for (int i = 0; i < j; i++) {
			if (s[i] < s[j]) {
				r++;
			}
		}
	}
	return r;
}

long ways(int sortedness, vector<int> seq)
{
	vector<int> blank , missing;
	int n = seq.size();

	// seq에서 값이 0인 인덱스를 blank vector에 저장한다.
	for (int i = 0; i < n; i++) {
		if (seq[i] == 0) {
			blank.push_back(i);
		}
	}

	// 없는 숫자들을 missing vector에 저장한다.
	for (int x = 1; x <= n; x++) {
		if ( count(seq.begin(), seq.end(), x) == 0) {
			missing.push_back(x);
		}
	}

	// calculate the initial sortedness 
	// 초기에 0이들어간 seq에서의 sorteness를 구한다.
	int initialSortedness = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if ( (seq[i] < seq[j]) && (seq[i] != 0) && (seq[j] != 0) ) {
				initialSortedness++;
			}
		}
	}


	// calculate the sortedness added by choosing a number in each of the blank places
	// 빈 공간에 들어올수 있는 모든 경우의 배열에서 각자의  sortedness를 계산한다.
	int m = blank.size();
	int **addSort = new int *[m];
	for (int i=0; i<m; ++i)
	{
		addSort[i] = new int[m];
	}
	//int addSort[m][m];
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < m; j++) {
			// assign missing[j] to position blank[i]
			addSort[i][j] = 0;
			for (int k = 0; k < n; k++) {
				if (seq[k] != 0) {
					if ( k < blank[i] ) {
						if ( seq[k] < missing[j] ) {
							addSort[i][j]++;
						}
					} else if (k > blank[i]) {
						if ( seq[k] > missing[j] ) {
							addSort[i][j]++;
						}
					}
				}
			}
		}
	}
	// we need to precalculate the sortedness of each permutation.
	// we *could* just use the permutation as a key for an associative array
	// but the following is a neat trick. We know that next_permutation will
	// always generate all permuations in the same order, so we can assign 
	// an unique id to each permutation by the order it is visited.
	int permScore1[5040];       
	vector<int> per1(m / 2);
	/*
	for (int i = 0; i < m / 2; i++) {
		per1[i] = i;
	}
	*/

	int pid = 0;
	for (int i = 0; i < m / 2; i++) {
		per1[i] = i;
	}
	
	do {
		permScore1[pid++] = getSortedness(per1);
		for (int i= 0; i<per1.size(); ++i)
		{
			printf("%d ", per1[i]);
		}
		printf("\n");
	} while ( next_permutation(per1.begin(), per1.end()) );

	// An issue is that the number of missing elements might be odd, so
	// the number of small and large elements might be different so we might
	// need to repeat for large numbers:
	int permScore2[5040];
	vector<int> per2( (m+1) / 2);
	for (int i = 0; i < (m+1) / 2; i++) {
		per2[i] = i;
	}
	pid = 0;
	printf("permScore2 start\n");
	do {
		permScore2[pid++] = getSortedness(per2);
		/*
		for (int i= 0; i<per2.size(); ++i)
		{
			printf("%d ", per2[i]);
		}
		
		printf("\n");
		*/
	} while ( next_permutation(per2.begin(), per2.end()) );


	long res = 0;
	// we can generate all combinations using next_permutation. Okay, this
	// solution is very next_permutation-specific, I admit.
	vector<int> comb(m);
	for (int i = 0; i < m/2; i++) {
		comb[i] = 0;
	}
	for (int j = m/2; j < m; j++) {
		comb[j] = 1;
	}
	do {
		const int MAX = 1999*7; //The maximum value of s. Roughly you can
		// imagine that for each of the m/2 small numbers we might add less
		// than n-1 sortedness. The real limit is smaller but is not needed
		// to find a tight bound.

		int combsort = getSortedness(comb); //sortedness by this combination

		// small : For each small permutation, find s and increment small[s]
		vector<long> small(MAX + 1);
		int pid = 0;
		for (int i = 0; i < m / 2; i++) {
			per1[i] = i;
		}
		do {
			int s = permScore1[pid++]; // small의 sortness를 더한다.
			int j = 0;
			for (int i = 0; i < m; i++) {
				if (comb[i] == 0) {  
					s += addSort[i][ per1[j++] ]; // 
				}
			}
			small[s]++;
		} while ( next_permutation(per1.begin(), per1.end()) );

		// large : For each large permutation, find the required s for a
		// matching small permutation and add small[s] to res
		pid = 0;
		for (int i = 0; i < (m+1) / 2; i++) {
			per2[i] = i;
		}
		do {
			int s = permScore2[pid++];
			int j = 0;
			for (int i = 0; i < m; i++) {
				if (comb[i] == 1) {
					s += addSort[i][ per2[j++] + (m/2) ];
				}
			}
			int ws = sortedness - initialSortedness - s - combsort;
			if ( 0 <= ws && ws <= MAX) {
				res += small[ws];
			}
		} while ( next_permutation(per2.begin(), per2.end()) );


	} while (next_permutation(comb.begin(), comb.end()));
	
	for (int i=0; i<m; ++i) {
		delete [] addSort[i];
	}
	delete [] addSort;

	return res;
}

int main()
{
	
	int nSortness = 100;
	vector<int> seq;
	int nSeq[] = {0, 13, 0, 0, 12, 0, 0, 0, 2, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 7, 15, 16, 20};
	
	/*
	int nSortness = 5;
	vector<int> seq;
	int nSeq[] = {4, 0, 0, 2, 0};
	*/

	seq.assign(nSeq, nSeq+sizeof(nSeq)/sizeof(nSeq[0]));

	clock_t start_time, end_time;      // clock_t 

	start_time = clock();                  // Start_Time

	int ret = ways(nSortness, seq);

	end_time = clock();                   // End_Time
	printf("Time : %f sec\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC); 
		
	printf("ret = %d" , ret);
	return 0;
}
