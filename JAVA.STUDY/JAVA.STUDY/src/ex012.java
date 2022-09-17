package br.com.feltex.snake.game;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.net.http.WebSocket.Listener;
import java.security.Key;
import java.util.Random;
import java.util.Timer;

import javax.swing.Action;
import javax.swing.JPanel;
import javax.swing.plaf.DimensionUIResource;

import org.w3c.dom.css.RGBColor;

public class teladojogo extends JPanel implements actionlistener {

    private static final int LARGURA_TELA = 1300;
    private static final int ALTURA_TELA = 750;
    private static final int TAMANHO_BLOCO = 50;
    private static final int UNDIDADES = LARGURA_TELA * ALTURA_TELA / (TAMANHO_BLOCO * TAMANHO_BLOCO);
    private static final int INTERVALO = 200;
    private static final String NOME_FONTE = "Ink Free";
    private  final int[] eixoX = new int[UNDIDADES];    
    private  final int[] eixoY = new int [UNDIDADES];
    private int corpoCobra = 6;
    private int blocosComidos;
    private int blocoX;
    private int blocoY;
    private char direcao = "D"; // C - cima, B - baixo, E - esquerda, D - direita
    private boolean estaRodando = false;
    Timer timer;
    Random random;
    private teladojogo Listener;

    Telajogo {
    random = new Random();
    setPreferredSize(new Dimension(LARGURA_TELA, ALTURA_TELA));
    setBackground(Color.white);
    setFocusCycleRoot(true);
    addKeyListener(new LeitorDeTecladoAdapter());
    iniciarJogo();
   }
/**
 * 
 */
   public void iniciarJogo() {
    criarBloco();
    estaRodando = true;
    timer = new Timer(INTERVALO, Listener:this);
    timer.Star();   
}

@Override
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    desenharTela(g);

  }

  public void desenharTela(Graphics g) {
    if  (estaRodando) {
      g.setColor(Color.red);
      g.fillOval(blocoX, blocoY, TAMANHO_BLOCO, TAMANHO_BLOCO);
      for (int i = 0; i < corpoCobra; i++) {
        if(i == 0) {
          g.setColor(Color.green);
          g.fillOval(eixoX[0], eixoY[0], TAMANHO_BLOCO, TAMANHO_BLOCO);
        } else {
          g.setColor(new Color(45, 180, 0));
          g.fillRect(eixoX[i], eixoY[i], TAMANHO_BLOCO, TAMANHO_BLOCO);

        }
      }
    }
    g.setColor(Color.red);
    g.setFont(new Font(NOME_FONTE, Font.BOLD, 40));
    FontMetrics metrics = getFontMetrics(g.getFont());
    g.drawStrings("Pontos: " + blocosComidos, (LARGURA_TELA - metrics.StringWidth("Pontuação: " + blocosComidos)) / 2, g.getFont().getSize());
   

  } else {
    FimDoJogo(g);
  }
}

private void criarBloco(){
  blocoX = random.nextInt(LARGURA_TELA / TAMANHO_BLOCO) * TAMANHO_BLOCO;
  blocoY = random.nextInt(ALTURA_TELA / TAMANHO_BLOCO) * TAMANHO_BLOCO;

}
public void FimDoJogo(Graphics g){
  g.setColor(Color.red);
    g.setFont(new Font(NOME_FONTE, Font.BOLD,40));
    FontMetrics FontePontuacao = getFontMetrics(g.getFont());
    g.drawStrings("Pontos: " + blocosComidos, (LARGURA_TELA - metrics.StringWidth("Pontuação: " + blocosComidos)) / 2, g.getFont().getSize());
    g.setColor(Color.red);
    g.getFont(new Font(NOME_FONTE, Font.BOLD, 75));
    FontMetrics FonteFinal  = getFontMetrics(g.getFont());
    g.drawStrings("\uD83D\uDE10 fim de jogo. " + blocosComidos, (LARGURA_TELA - metrics.StringWidth("Pontuação: " + blocosComidos)) / 2, ALTURA_TELA / 2);
}


public void actionPerformed(ActionEvent e) {
  if(estaRodando) {
    andar();
    alcancarbloco();
    validarLimites();
  }
  repaint();
}
private void andar() {
  for (int i = corpoCobra; i > 0; i--){
    eixoX[i] = eixoX[i - 1];
    eixoY[i] = eixoY[i - 1];
  
  switch (direcao) {
    case "C":
    eixoY[0] = eixoY[0] - TAMANHO_BLOCO;
    break;

    case "B":
    eixoY[0 ] = eixoY[0] - TAMANHO_BLOCO;
    break;

    case "E":
    eixoX[0] = eixoX[0] - TAMANHO_BLOCO;
    break;

    case "D":
    eixoY[0] = eixoY[0] - TAMANHO_BLOCO;
    break;
    }
  Default:
  break;  
  } 
}
 

private void alcancarbloco() {
    if (eixoX[0] == eixoY[i] && eixoY[0] == blocoY) {
        corpoCobra++;
        blocosComidos++;
        criarBloco();
      }
}

private void validarLimites() {
for(int i = corpoCobra; i > 0; i--){
  if (eixoX[0] == eixoY[i] && eixoY[0] == eixoX[i]) {
    estaRodando = false;
    break;
  }

if (eixoX[0] < 0 || eixoX[0] > LARGURA_TELA) {
    estaRodando = false;
  }
}

if (eixoY[0] < 0 || eixoY[0] > ALTURA_TELA) {
  estaRodando = false;
  }

if (!estaRodando) {
  timer.stop();
  }
}

public class LeitorDeTecladoAdapter extends KeyAdapter {
    @Override
    public void KeyPressed(KeyEvent e) {
      switch(e.getKeyCode()) {
        case KeyEvent.VK_LEFT:
          if(direcao != "D") {
            direcao = "E";
          }
          break;

          case KeyEvent.VK_RIGHT:
          if(direcao != "E") {
            direcao = "D";
          }
          break;

          case KeyEvent.VK_UP:
          if(direcao != "B") {
            direcao = "C";
          }
          break;

          case KeyEvent.VK_DOWN:
          if(direcao != "C") {
            direcao = "B";
          }
          break;
        default:
          break; 
        }
      }
    }        
  }
}
