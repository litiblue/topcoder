import java.math.BigInteger;
import java.util.*;
import java.util.Map.Entry;

public class Egalitarianism3Easy {

	public static int maxCities(int n, int[] a, int[] b, int[] len) {
		
		HashMap<Integer, Integer> org_map = new HashMap<Integer, Integer>();
		final int N_BASIC = n+1;

		for (int i = 0; i < n - 1; ++i) {
			int key = ((a[i]) * N_BASIC)  + b[i];
			org_map.put(key, len[i]);
		}

		Iterator<Map.Entry<Integer, Integer>> entries1 = org_map.entrySet()
				.iterator();

		for (int i = 0; i < n; ++i) {
			while (entries1.hasNext()) {
				Map.Entry<Integer, Integer> entry1 = entries1.next();
				int start1 = entry1.getKey() / N_BASIC;
				int end1 = entry1.getKey() % N_BASIC;

				Iterator<Map.Entry<Integer, Integer>> entries2 = org_map
						.entrySet().iterator();
				while (entries2.hasNext()) {

					Map.Entry<Integer, Integer> entry2 = entries2.next();
					int start2 = entry2.getKey() / N_BASIC;
					int end2 = entry2.getKey() % N_BASIC;

					int new_key = 0;
					int new_len = 0;

					if ((start1 == start2) && (end1 == end2))
						continue;
					else if (start1 == start2) {
						new_key = (end1 > end2) ? (end2 * N_BASIC + end1) : (end1 * N_BASIC + end2);
						new_len = entry1.getValue() + entry2.getValue();
					} else if (end1 == end2) {
						if (start1 > start2)
						new_key = (start1 > start2) ? (start2 * N_BASIC + start1) : (start1 * N_BASIC + start2);
						new_len = entry1.getValue() + entry2.getValue();
					} else if (end1 == start2) {
						new_key = (start1< end2) ? (start1 * N_BASIC + end2): end2 * N_BASIC + start1; 
						new_len = entry1.getValue() + entry2.getValue();
					}

					if (0 == new_key)
						continue;
					else if ((org_map.containsKey(new_key) == true)
							&& (org_map.get(new_key) > new_len)) {
						org_map.put(new_key, new_len);
						entries2 = org_map.entrySet().iterator();
						entries1 = org_map.entrySet().iterator();
					} else if (org_map.containsKey(new_key) == false) {
						org_map.put(new_key, new_len);
						entries2 = org_map.entrySet().iterator();
						entries1 = org_map.entrySet().iterator();
					}
				}
			}
		}
		
		int  ret = 0; 
		for (long k=0 ; k< (1<<n); ++k) // 2^n 개의 city 조합의 개수
		{
			int x =-1, c=0;
			boolean bDiffrent = false;
			for(int i=0; i<n; ++i)
			{
				if (1 <= (k & (1<<i))) // 하나의 도시를 선택한다.
				{
					c++;
					for (int j=0; j<n ;++j)
					{
						if((i!=j) &&  (1 <= (k &(1<<j)))) // 다른 도시를 선택
						{
							int find_key = i>j ? (j+1)*N_BASIC+i+1 : (i+1)*N_BASIC+j+1;
							int distance =org_map.get(find_key); 
							
							if (-1 == x) 
								x = distance;
							else if (x != distance) {
								bDiffrent = true;
								break;
							}
						}
							
					}
				}		
			}
			if (bDiffrent == false)
				ret = ret > c ? ret : c; 
		}
		return ret;
	}
}
