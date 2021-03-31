

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;

public class Filtro{
	BufferedImage imagen;
	BufferedImage borrador;
	BufferedImage borrador2;
	BufferedImage borrador3;
	BufferedImage borrador4;
	BufferedImage borrador5;
	BufferedImage borrador6;
	BufferedImage borrador7;
        BufferedImage borrador8;
        String drx = "D:\\compila2 java(hackerter)\\programa de filtros\\weas de progra\\proyecto de filtro\\goku1.jpg";
	
	int ancho;
	int alto;
        
	public void ObtenerImagen(){
		try{
		//Con ImageIO y un objeto de la clase FileInputStream, coloco la imagen en el BufferedImage
		imagen = ImageIO.read(new FileInputStream(drx));
		borrador = ImageIO.read(new FileInputStream(drx));
		borrador2 = ImageIO.read(new FileInputStream(drx));
		borrador3 = ImageIO.read(new FileInputStream(drx));
		borrador4 = ImageIO.read(new FileInputStream(drx));
		borrador5 = ImageIO.read(new FileInputStream(drx));
		borrador6 = ImageIO.read(new FileInputStream(drx));
		borrador7 = ImageIO.read(new FileInputStream(drx));
                borrador8 = ImageIO.read(new FileInputStream(drx));
		}
		//Por si no está la imagen
		catch(FileNotFoundException fnfe){System.out.print(fnfe.getMessage());}
		//Por si hay excepciones de entrada o salida
		catch(IOException ioe){System.out.print(ioe.getMessage());}
	}
	public void Tamano(){
		ancho = borrador.getWidth(null); 
		alto = borrador.getHeight(null);
		//System.out.println("ancho "+ancho+" y alto "+alto);
	}
	
}
		
