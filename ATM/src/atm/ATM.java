
package atm;

import java.util.Scanner;

public class ATM {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in); 
   System.out.print("==SELAMAT DATANG DI ATM==");
        String nama = input.nextLine();
        int Saldo = 20000;
        
        System.out.print("Masukkan saldo : ");
        int saldo = input.nextInt();
        
        short batasTransaksi = 5;
        
        while (batasTransaksi > 0){
            
            int saldoSekarang = saldo;
            System.out.print("MENU TRANSAKSI\n"
                    + "1. Penarikan\n"
                    + "2. Menabung\n"
                    + "3. Pilih [1,2] : ");
            String menu = input.next();
            
            if (menu.equalsIgnoreCase("1")) {
                System.out.println("Anda akan melakukan penarikan tunai\n"+"Saldo anda adalah RP. "+ saldo +"\nMasukkan jumlah penarikan : ");
                
                int penarikan = input.nextInt();
                
                if (saldo - penarikan < 5000) {
                    System.out.println("Sisa saldo harus minimal Rp.5000");
                    
                }else if (penarikan < 2000) {
                    System.out.println("Penarikan harus minimal Rp.2000");
                    
                }else {
                    saldo = saldo - penarikan;
                    System.out.println("Saldo awal anda adalah Rp. "+saldoSekarang +" . Anda melalukan penarikan sebesar Rp. "+penarikan);
                }
                
                System.out.println("Sisa saldo anda adalah Rp. "+ saldo +"Sisa Transaksi anda masih "+ (batasTransaksi -1) + " kali.");
                
            }else if (menu.equalsIgnoreCase("2") ) {
                System.out.println("Anda akan melakukan setor tunai\n"+"Saldo anda adalah Rp. "+saldo +"\nMasukkan jumlah setor : ");
                
                int setor = input.nextInt();
                
                if (setor < 2000) {
                    System.out.println("Setor harus minimal Rp.2000");
                    
                }else {
                    saldo = saldo + setor;
                    System.out.println("Saldo awal anda adalah Rp. "+saldoSekarang +" . Anda melakukan setor sebesar Rp. "+setor);
                }
                
                System.out.println("Jumlah saldo anda adalah Rp. "+saldo +" Sisa Transaksi anda masih "+ (batasTransaksi -1) + " kali.");
                
            }else {
                System.out.println("Maaf pilihan menu anda salah");
            }
          
            //Step
            System.out.println("Apakah anda akan bertransaksi lagi? y/n : ");
            
            String pilihan = input.next();
            
            if (pilihan.equalsIgnoreCase("n")){
                System.out.println("Terima Kasih Telah Bertransaksi ");
                batasTransaksi = 0;
                
            }else {
                System.out.println("Pilihan tidak ada");
                batasTransaksi = 0;
            }   
       }
    }
}
