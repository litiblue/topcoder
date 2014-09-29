import java.util.*;

public class Egalitarianism3 {

	public static int maxCities(int n, int[] a, int[] b, int[] len) {
		
		HashMap<Integer, Integer> org_map = new HashMap<Integer, Integer>();
		final int N_BASIC = n+1;

		for (int i = 0; i < n - 1; ++i) {
			int key1 = ((a[i]) * N_BASIC)  + b[i];
			int key2 = ( b[i] * N_BASIC)  + (a[i]);
			org_map.put(key1, len[i]);
			org_map.put(key2, len[i]);
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
		
		int max_city = 0;
		for (int x = 1; x <=n ; ++x)
		{
			HashMap<Integer, Vector<Integer>> dist = new HashMap<Integer, Vector<Integer>>();
			for(int k=1 ; k<=n; ++k)
			{
				if (x == k) continue;
				Vector<Integer> city = new Vector<Integer>();
				int Dx_yKey = x > k ? (k *N_BASIC+x) : (x*N_BASIC+k);
				int Dx_y = org_map.get(Dx_yKey);
				if (dist.containsKey(Dx_y) == true) {
					city = dist.get(Dx_y);
					city.add(k);							
				}
				else {
					city.add(k);
					dist.put(Dx_y, city);					
				}
			}
		
			Iterator <Integer> itKey = dist.keySet().iterator();
			
			while( itKey.hasNext() ){
		
				Vector<Integer> city = new Vector<Integer>();
				Vector<Integer> same_city = new Vector<Integer>();
							
				city = dist.get(itKey.next());
				
				int y_size = city.size();
				for (int y_index = 0; y_index < y_size; ++y_index) {
					int y = city.get(y_index);

					int Dx_yKey = x > y ? (y * N_BASIC + x) : (x * N_BASIC + y);
					int Dx_y = org_map.get(Dx_yKey);
					
					int size = same_city.size();
					boolean match = true ;
					for (int j = 0; j < size; ++j) {
						int z = same_city.get(j);
						int Dy_zKey = z > y ? (y * N_BASIC + z): (z * N_BASIC + y);
						if ((2 * Dx_y) != org_map.get(Dy_zKey)) match = false;
						
					}
					if (true == match) same_city.add(y);
				}
				
				max_city = Math.max(max_city, same_city.size());
	        }
		}
		return max_city;
	}
}
