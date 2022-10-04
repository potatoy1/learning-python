package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	String com = "123";
	private JTextArea ta;
	private JButton btnReset;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 308, 509);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("세자리수:");
		lbl.setBounds(34, 36, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(141, 33, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞추기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(34, 84, 106, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(34, 136, 223, 292);
		contentPane.add(ta);
		
		btnReset = new JButton("리셋");
		btnReset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myreset();
			}
		});
		btnReset.setBounds(160, 84, 97, 23);
		contentPane.add(btnReset);

		setCom();
	}
	
	public void myreset() {
		tf.setText("");
		ta.setText("");
		setCom();
	}
	
	public int getBall(String com, String mine) {
		int cnt = 0;

		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m2)||c1.equals(m3)) cnt++;
		if(c2.equals(m1)||c2.equals(m3)) cnt++;
		if(c3.equals(m1)||c3.equals(m2)) cnt++;
		
		return cnt;
	}
	
	public int getStrike(String com, String mine) {
		int cnt = 0;

		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m1)) cnt++;
		if(c2.equals(m2)) cnt++;
		if(c3.equals(m3)) cnt++;
		
		return cnt;
	}
	
	public void myclick() {
		String str_old = ta.getText();
		
		String mine = tf.getText();
		int s = getStrike(com,mine);
		int b = getBall(com,mine);
		
		String str_new = mine + " " + s+"S"+b+"B \n";
		ta.setText(str_old +str_new);
		
		tf.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(null, mine+"를 맞혔습니다.");
		}
	}
	
	public void setCom() {

		int[] arr9 = {1,2,3,4,5,6,7,8,9};

		 	for(int i = 0;i<100;i++) {
				int rnd = (int)(Math.random()*9);
				int a = arr9[0];
				int b = arr9[rnd];
				arr9[0]=b;
				arr9[rnd]=a;
			}
		 	
		 	com = arr9[0]+""+arr9[1]+""+arr9[2];
		 	System.out.println(com);
	}
}
