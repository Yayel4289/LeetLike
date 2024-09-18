public class architecture{

	public static String solution(int[][] tab,int x, int y, int[] R, int[]C){
		for(int i = 0; i< x;i++){
				int maxh = maxHori(tab,y,i);
				int maxv = maxVer(tab,x,i);
			//	System.out.println(maxh);
			//	System.out.println(maxv);
				if(R[i] > maxh){
					return "impossible";
					}
			       if(C[i] > maxv){
			       	       return "impossible";
			      	 	}	
			}
	return "possible";	
		}
	
	public static int maxHori(int[][] R,int y, int inter){
		int max = R[0][0];
		for(int i = 0; i < y; i++){
			if(R[inter][i] > max){
				max = R[inter][i];
				}
			}
		
		return max;
		}
	public static int maxVer(int[][] R, int x, int inter){
		int max  = R[0][0];
		for(int i= 0; i< x; i++){
			if(R[i][inter] > max){
				max = R[i][inter];
				}
			}
		return max;
		}

	public static void main(String[] args){
		int[] C = {1,2,3,4};
		int[] R = {1,2,3,2};
		int[][] tab = {{1,2,3,4},{0,1,2,3},{1,2,1,1},{1,0,1,1}};	
		System.out.println(solution(tab,4,4,C,R));
		}

	/*Methode statique car pas d'accès au tableau de l'exercice :)*/	
}
