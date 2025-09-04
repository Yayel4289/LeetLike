import java.util.List;
import java.util.ArrayList;
public class ExitinExcess{
	
	int n,m;
	List<Integer> content;

	public ExitinExcess(int n, List<Integer> content){
		this.n = n;
		this.content = content;
		}
	
	public ExitinExcess(int n, int m){
		this.n = n;
		this.m = m;
	}

	public static List<Integer> listCreating(int[][] tab,int j){
		List<Integer> A = new ArrayList<>();	
		for(int i = 0; i<tab.length; i++){
			A.add(tab[i][j]);	
		}
		return A;
	} 

	public static ExitinExcess solution(int a , int b , int[][] tab){
		List<ExitinExcess> C = secondListCreating(b,tab);
		List<Integer> res = new ArrayList<>();
		int i = 0;
		int j = 0;
		int d = 0;
		if(C.size() == 0){
			res.add(0);
			return new ExitinExcess(0,res);
		}
		while((d<b/2)){
			if((j+= 1) == b){
				j =0;
				i+= 1;	
				} 
			if(tab[i][1] == (C.get(j).n)){
				d += 1;
				res.add(i+1);
				i+=1;
				j = 0;
			}
			if(d == 0 && ((i+= 1) == b)){
				break;
				}
			j+= 1;	
		}
		return new ExitinExcess(d,res);

	}

	public static List<ExitinExcess> secondListCreating(int a,int[][] tab){
		List<Integer> A = listCreating(tab,0);
	        List<Integer> B = listCreating(tab,1);
		List<ExitinExcess> C = new ArrayList<>();
		for(int i = 0; i< a; i++){
			for(int j = 0; j<a; j++){
				if(A.get(j) == B.get(i)){
					int interA = A.get(i);
					int interB = B.get(j);
					//System.out.println(interA + " " + interB);
					ExitinExcess c = new ExitinExcess(interA,interB);
					C.add(c);
					}
				}
			}
		return C;	
	}

	

	public String toString(){
		return n + " " + content;	
	}


	public static void main(String[] args){
		int[][] tab = {{1,2},{2,3},{2,4},{3,1},{4,1}};
		int[][] tab2 = {{1,2},{2,3},{3,1}};
		int[][] tab3 = {{1,2},{1,3},{3,2},{2,4},{3,4}}; 	
		int[][] tab4 = {{1,2},{2,1}};
		int[][] tab5 = {{1,2},{2,3},{3,4}};
		System.out.println(listCreating(tab5,0));	
	        System.out.println(listCreating(tab5,1));	
		System.out.println(solution(4,3,tab5));
	}
	

}
