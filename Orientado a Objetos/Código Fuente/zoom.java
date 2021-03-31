
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Hackerter
 */
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import javax.swing.JPanel;

public class zoom extends JPanel {

    private Image FOTO_ORIGINAL;
    private Image FOTO_tmp;
    private BufferedImage Imagen_en_memoria;
    private Graphics2D g2D;
    private boolean con_foto = false;   

    private int valEscalaX=0;
    private int valEscalaY=0;

    /* al crear el objeto se crea con una imagen pasada como parametro*/
    public zoom(BufferedImage f){
        this.FOTO_ORIGINAL = f;
        this.FOTO_tmp = f;
        this.setSize(f.getWidth(),f.getHeight());
        this.setVisible(true);
        this.con_foto=true;
    }

    @Override
    protected void paintComponent(Graphics g) {
      Graphics2D g2 = (Graphics2D)g;
      if(this.con_foto){
        Imagen_en_memoria = new BufferedImage(this.getWidth(), this.getHeight(), BufferedImage.TYPE_INT_RGB);
        g2D = Imagen_en_memoria.createGraphics();
        g2D.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        //se añade la foto
        g2D.drawImage(FOTO_tmp,0, 0, FOTO_tmp.getWidth(this), FOTO_tmp.getHeight(this), this);
        g2.drawImage(Imagen_en_memoria, 0, 0, this);

      }
    }

    public void Aumentar(int Valor_Zoom){
        //se calcula el incremento
        valEscalaX = 0;
        valEscalaY = 0;
        valEscalaX =  (int) (FOTO_tmp.getWidth(this) * escala(Valor_Zoom) );
        valEscalaY =  (int) (FOTO_tmp.getHeight(this) * escala(Valor_Zoom) );
        //se escala la imagen sumado el nuevo incremento
        this.FOTO_tmp = FOTO_tmp.getScaledInstance((int) (FOTO_tmp.getWidth(this) + valEscalaX), (int) (FOTO_tmp.getHeight(this) + valEscalaY), Image.SCALE_AREA_AVERAGING);
        resize();
    }

    public void Disminuir(int Valor_Zoom){
        valEscalaX = 0;
        valEscalaY = 0;
        valEscalaX =  (int) (FOTO_tmp.getWidth(this) * escala(Valor_Zoom) );
        valEscalaY =  (int) (FOTO_tmp.getHeight(this) * escala(Valor_Zoom) );
        this.FOTO_tmp = FOTO_tmp.getScaledInstance((int) (FOTO_tmp.getWidth(this) - valEscalaX), (int) (FOTO_tmp.getHeight(this) - valEscalaY), Image.SCALE_AREA_AVERAGING);
        resize();
     }

    private float escala(int v){
        return  v/100f;
    }

    public void Restaurar(){
        this.FOTO_tmp = this.FOTO_ORIGINAL;
        resize();
    }

    private void resize(){
        this.setSize(FOTO_tmp.getWidth(this),FOTO_tmp.getHeight(this));
    }
    public void exit(){
        System.exit(0);
    }
       
}