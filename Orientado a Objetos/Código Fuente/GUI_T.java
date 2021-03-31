import javax.swing.*;
import javax.swing.event.*;
import java.awt.event.*;
//import java.awt.image.BufferedImage;
//import java.awt.*;
//import java.awt.image.*;
//import java.io.*;
//import javax.imageio.*;

//esta forma es donde se crean los objetos para ser invocados desde las otras clases de procedimientos

class GUI_T extends JFrame implements ActionListener {
	JPanel panel;
	JPanel panel2;
	JPanel panel3;
	JPanel panel4;
	JPanel panel5;
	JPanel panel6;
        JPanel panel7;
        
        JSlider slider1;
	JSlider slider2;
	JSlider slider4;
	
	JFrame frame;
        
        JScrollPane dim;
	
	JButton bt1;
	JButton bt2;
	JButton bt3;
	JButton bt4;
	JButton bt5;
        JButton bt6;
        JButton btrepain;
        JButton btrepain2;
        JButton btrepain3;
	
	JLabel lb1;
	JLabel lb2;
	JLabel lb3;
	JLabel lb4;
	JLabel lb5;
	JLabel lbl1;
	JLabel slid_b = new JLabel("Brillo         ");
	JLabel slid_c = new JLabel("Contraste");
        JLabel slid_d = new JLabel("Tamaño");
	
        int lab = 0;
        int lab1 = 0;
        int cr = 0;
        int cr1 = 0;
        
	int vlr = 0;
	int vlr1 = 0;
        int br = 0;
        int br1 = 0;
        int start = 0;
	
	Filtro goku;
	WB goku1;
	Grises gr;
	invertir ng;
        zoom sof;
        brillo slim;
        contraste ngr;
	
	
	public static void main(String args[]){
		GUI_T gui = new GUI_T();
		gui.go();
	}
	
	public void go(){
		panel = new JPanel(); //crea panel principal
		panel.setBounds(0,25,350,450);
		panel.setVisible(true);
		
		panel2 = new JPanel(); //crea panel negativo
		panel2.setBounds(400,60,350,450);
		panel2.setVisible(false);
		
		panel3 = new JPanel(); // crea panel B&N
		panel3.setBounds(400,60,350,450);
		panel3.setVisible(false);
		
		panel4 = new JPanel(); //crea escala de grises
		panel4.setBounds(400,60,350,450);
		panel4.setVisible(false);
		
		panel6 = new JPanel(); //crea panel brillo&contraste
		panel6.setBounds(400,10,350,450);
		panel6.setVisible(false);
                
                panel7 = new JPanel(null); //crea panel de Redimencion
                panel7.setBounds(400,10,350,450);
                panel7.setVisible(false);
		
		frame = new JFrame("Photo Filtre"); //crea el frame con titulo
		frame.setLayout(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		slider1 = new JSlider(JSlider.HORIZONTAL, -100, 100, start);
		slider1.setMinorTickSpacing(5);// determina los intervalos de valores pequeños
                slider1.setMajorTickSpacing(50); // determina los intervalos de valores mayores
                slider1.setPaintTicks(true); // muesta los miniSlid
                slider1.setPaintLabels(true); //muestra la tabla de Slid-miniSlid
                slider1.setLabelTable(slider1.createStandardLabels(50)); //determina el rango de valores MAYORES
                slider1.addChangeListener(new MyChangeAction());
        
                slider2 = new JSlider(JSlider.HORIZONTAL, -100, 100, start);
		slider2.setMinorTickSpacing(5);// determina los intervalos de valores pequeños
                slider2.setMajorTickSpacing(50); // determina los intervalos de valores mayores
                slider2.setPaintTicks(true); // muesta los miniSlid
                slider2.setPaintLabels(true); //muestra la tabla de Slid-miniSlid
                slider2.setLabelTable(slider1.createStandardLabels(50)); //determina el rango de valores MAYORES
                slider2.addChangeListener(new MyChangeAction());
                   //se eliminó el Slider 3 xq no tenia razon de estar
                slider4 = new JSlider(JSlider.HORIZONTAL, -10 ,10, start);
                slider4.setMinorTickSpacing(1);// determina los intervalos de valores pequeños
                slider4.setMajorTickSpacing(5); // determina los intervalos de valores mayores
                slider4.setPaintTicks(true); // muesta los miniSlid
                slider4.setPaintLabels(true); //muestra la tabla de Slid-miniSlid
                slider4.setLabelTable(slider4.createStandardLabels(5)); //determina el rango de valores MAYORES
                slider4.addChangeListener(new MyChangeAction());
                slider4.setBounds(60,400,200,50);
		
		bt1 = new JButton("Negativo"); //nombre a los botones
		bt2 = new JButton("Blanco & Negro");
		bt3 = new JButton("Grises");
		bt4 = new JButton("Brillo & Contraste");
                bt5 = new JButton("Redimencion");
                bt6 = new JButton ("Exit");
                btrepain3 = new JButton("Pintar C");
                btrepain2 = new JButton("Pintar B");
                btrepain = new JButton("Pintar");
                                	
		goku = new Filtro();
		goku1 = new WB();
		ng = new invertir();
		gr = new Grises();
                slim = new brillo();
                ngr = new contraste();
                				
		goku.ObtenerImagen(); //carga procecso de carga de imagen en filtro
		goku.Tamano();//obtiene las variables de alto y ancho de filtro
                
                sof = new zoom(goku.borrador8);
		
		ng.SetInvertir(goku.borrador);
		//goku.borrador = ng.getFoto();	
		
		gr.set_Escala_de_Grises(goku.borrador2);
			
		lb1 = new JLabel (new ImageIcon(goku.imagen)); //rellena los labels con imagenes, label original
		lb1.setBounds(0,0,goku.alto,goku.ancho);
		lb2 = new JLabel (new ImageIcon(ng.getFoto())); // rellena label negativo
		lb2.setBounds(0,0,goku.alto,goku.ancho);
		lb3 = new JLabel (new ImageIcon(goku1.set_Blanco_y_Negro_con_Umbral(goku.borrador3))); // rellena label blanco&negro
		lb3.setBounds(0,0,goku.alto,goku.ancho);
		lb4 = new JLabel (new ImageIcon(gr.getFotoGris())); // rellena label escala de grises
		lb4.setBounds(0,0,goku.alto,goku.ancho);
		
		lbl1 = new JLabel (new ImageIcon(goku.imagen)); //rellena el label Brillo&Contraste
		lbl1.setBounds(0,0,goku.alto,goku.ancho);
		
                slid_d.setBounds(260,380,200,60);
                                           
		bt1.addActionListener(this);//(Negatvo)acciona el ActionListener en botones
		bt2.addActionListener(this);//Blanco y negro
		bt3.addActionListener(this);//grises
		bt4.addActionListener(this);//brillo y contraste
		bt5.addActionListener(this);//Redimencion
                bt6.addActionListener(this);//Exit
                
                btrepain.addActionListener(this); // repinta el panel de Redimencion
                btrepain.setVisible(true);
                btrepain2.addActionListener(this);
                btrepain2.setVisible(true);// reparar el boton pintar brillo
                btrepain3.addActionListener(this);
                btrepain3.setVisible(true);
                
		
		bt1.setBounds(5,330,70,20);//botones del frame principal
		bt2.setBounds(75,330,70,20);//da ubicaciones manuales, setBounds( x , y , ancho , alto );
		bt3.setBounds(145,330,70,20);
		bt4.setBounds(215,330,70,20);
		bt5.setBounds(285,330,70,20);
                bt6.setBounds(60,400,200,50);
                btrepain.setBounds(115,375,100,25);
		
		panel.add(bt1); //(Negativo) adiere objetos o botones a los paneles
		panel.add(bt2);//Blanco y negro
		panel.add(bt3);//grises 
		panel.add(bt4);//Brillo y contraste
		panel.add(bt5);//Redimencion
                panel.add(bt6);//Exit
                panel6.add(btrepain3);
                panel6.add(btrepain2);
		panel6.add(slider1);//slider Brillo
		panel6.add(slid_b);//label brillo
		panel6.add(slider2);//Slider contraste
		panel6.add(slid_c);//label contraste
                panel7.add(slider4);//slider redimencion
                panel7.add(btrepain);
                panel7.add(slid_d);
                panel7.add(sof);//imagen redimencion
                		
		panel.add(lb1); //se agregan los labels a los paneles
		panel2.add(lb2);
		panel3.add(lb3);
		panel4.add(lb4);
		panel6.add(lbl1);
		
		frame.add(panel); // se agregan los paneles a los Frames
		frame.add(panel2);
		frame.add(panel3);
		frame.add(panel4);
		frame.add(panel6);
                frame.add(panel7); //en vez del panel 7 
		
		frame.setSize(750,500);//tamaño ventana
		frame.setLocation(100,100);//posicion pantalla
		frame.setVisible(true);//da visibilidad de la ventana
		frame.setResizable(false);//evita redimencionar la ventana
		
		
	}
    @Override
   	public void actionPerformed(ActionEvent e){
                if(e.getSource()==btrepain){
                    System.out.println("Vlr "+vlr);
                    System.out.println("Vlr1 "+vlr1);
                    if(vlr==0){
                        sof.Restaurar();
                        panel7.repaint();
                    }else if(vlr > vlr1 ){
                        if(vlr<0){
                            sof.Aumentar(-vlr);
                            panel7.repaint();
                        }else{
                            sof.Aumentar(vlr);
                            panel7.repaint();
                        }
                    }else if(vlr < vlr1){
                        if(vlr<0){
                            sof.Disminuir(-vlr);
                            panel7.repaint();
                        }else{
                            sof.Disminuir(vlr);
                            panel7.repaint();
                        }
                    }
                    vlr1 = vlr;
                }
                else if(e.getSource()==btrepain2){/**************************/
                    System.out.println("Br "+br);
                    System.out.println("Br1 "+br1);
                    if(br > br1 ){
                        lbl1.setIcon(new ImageIcon(slim.activar(goku.borrador8,br)));
                    }else if(br < br1){
                        lbl1.setIcon(new ImageIcon(slim.activar(goku.borrador8,br)));
                    }
                    br1 = br;
                }
                else if(e.getSource()==btrepain3){
                    System.out.println("cr "+cr);
                    System.out.println("cr1 "+cr1);
                    if(cr > cr1 ){
                        lbl1.setIcon(new ImageIcon(ngr.activar(goku.borrador8,cr)));
                    }else if(cr < cr1){
                        lbl1.setIcon(new ImageIcon(ngr.activar(goku.borrador8,cr)));
                    }
                    cr1 = cr;
                }
                else{
                    
                    panel2.setVisible(false);
                    panel3.setVisible(false);
                    panel4.setVisible(false);
                    panel6.setVisible(false);
//                    dim.setVisible(false);
                    panel7.setVisible(false);


                    if(e.getSource()==bt1){
                            JOptionPane.showMessageDialog(null,"Filtro negativo pegado","Resultado",JOptionPane.INFORMATION_MESSAGE);
                            panel2.setVisible(true);
                            goku.ObtenerImagen(); 

                            //System.out.println(goku.borrador.getWidth(null)+" "+goku.borrador.getHeight(null));
                    }else if(e.getSource()==bt2){
                            JOptionPane.showMessageDialog(null,"Filtro Blanco y negro pegado","Resultado",JOptionPane.INFORMATION_MESSAGE);
                            panel3.setVisible(true);
                            goku.ObtenerImagen();

                    }else if(e.getSource()==bt3){
                            JOptionPane.showMessageDialog(null,"Filtro Escala de grises pegado","Resultado",JOptionPane.INFORMATION_MESSAGE);
                            panel4.setVisible(true);
                            goku.ObtenerImagen();
                    }else if(e.getSource()==bt4){
                            JOptionPane.showMessageDialog(null,"Filtro Brillo&Contraste","Resultado",JOptionPane.INFORMATION_MESSAGE);
                            panel6.setVisible(true);
                            goku.ObtenerImagen();
                    }
                    else if(e.getSource()==bt5){
                            JOptionPane.showMessageDialog(null,"Filtro Redimencion","Resultado",JOptionPane.INFORMATION_MESSAGE);
                            panel7.setVisible(true);
//                            dim.setVisible(true);
                            goku.ObtenerImagen();
                    }
                    else if(e.getSource()==bt6){
                            sof.exit();
                    }
                    
                    
		}
	}
	public class MyChangeAction implements ChangeListener{ // actualiza el slider en tiempo real
        @Override
		public void stateChanged(ChangeEvent ce){
                        vlr = slider4.getValue(); // slider de redimencion
                        String str = Integer.toString(vlr);
                        slid_d.setText(str);
                        
                        br = slider1.getValue(); // slider de brillo
                        String str1 = Integer.toString(br);
                        slid_b.setText(str1);
                        
                        cr = slider2.getValue();//slider contraste
                        String str2 = Integer.toString(cr);
                        slid_c.setText(str2);
                }
	}
	
}
