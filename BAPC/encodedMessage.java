import java.lang.Math;
public class encodedMessage{

		public static String decodedMessage(String string){
			String res = "";
			int string_size = string.length();
			int sqrt_sts = (int) Math.sqrt(string_size);
			int inter = 0;
			for(int i = sqrt_sts-1; i>=0; i--){
				inter = i;
				for(int j = 0 ; j < sqrt_sts; j++){
					res += string.charAt(inter);
					inter += sqrt_sts; 
					}
				}
			return res;
			
		}
		public static void solution(int n, String... string){
			/*if(string.length != n){
				throw new Exception("incorrect");
				}*/
			for(int i = 0 ; i<n; i++){
				String res = string[i];
				System.out.println(decodedMessage(res));
				}
			}

		public static void main(String[] args){
			String one = "RSTEEOTCP";
			String two = "eedARBtVrolsiesuAoReerles";
			String three = "EarSvyeqeBsuneMa";
			solution(3,one,two,three);
				
		}

}
