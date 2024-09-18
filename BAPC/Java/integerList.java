import java.util.List;
import java.util.ArrayList;
public class integerList{

	public static List<Integer> BAPC(String string, int n , int[] liste){
		List<Integer> res = new ArrayList<>();
		int start = 0;
		int ending = 1;
		for(int i= 0; i<liste.length; i++){
			res.add(liste[i]);
			}
		if(liste.length == 0){
			System.out.println("error");
			return null;
			}
		else{
			for(int  i = 0; i<string.length(); i++){
				if(string.substring(start,ending).equals("R")){
					int end = res.size()-1;
					for(int  j = 0; j<res.size();j++){
						int inter = res.get(j);
						res.set(j,res.get(end));
						res.set(end,inter);
						end--;
						if(end == j){
							break;
							}	
						}
					}
				if(string.substring(start,ending).equals("D") && res.size() != 0){
					res.remove(res.get(0));
					}
				if(res.size() == 0){
					System.out.println("error");
					break;
					}
				start = ending;
				ending++;
				}
			}
		return res;	
	}

	public static void display(List<Integer> liste){
		for(int c : liste){
			System.out.println(c);
			}
		}

	public static void main(String[] args){
		int[] array = {1,2,3,4};
		int[] array2 = {1,1,2,3,5,8};
		int[] array3 =  {42};
		List<Integer> res = BAPC("RDD",4,array);
		List<Integer> res2 = BAPC("RRD",6,array2);
		List<Integer> res3 = BAPC("DD",1,array3);
		//display(res2);	
	}
}
