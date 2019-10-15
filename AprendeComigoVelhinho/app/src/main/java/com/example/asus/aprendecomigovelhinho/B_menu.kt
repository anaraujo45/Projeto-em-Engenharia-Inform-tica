package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.app.AlertDialog
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_b_menu.*

class B_menu : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_b_menu)

    }

    fun b_avancar_c(view: View) {
        val nomeIdoso :String
        nomeIdoso=editTextNomeVelhinho.text.toString()

        if(editTextNomeVelhinho.text.isEmpty()) {

            val builder = AlertDialog.Builder(this@B_menu)
            builder.setTitle("Atenção")
            builder.setMessage("Deve colocar o seu nome para continuar")
            builder.setPositiveButton("Continuar") { dialog, which ->
                //Toast.makeText(applicationContext, "continuar", Toast.LENGTH_SHORT).show()
            }
            val dialog: AlertDialog = builder.create()
            dialog.show()

        }
        else {
            val it = Intent(this, C_aviso::class.java)
            startActivity(it)
        }
    }
}


/*
*             AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(MainActivity.this);
            alertDialogBuilder
                    .setMessage("Fim do jogo!\nP1: " + playerPoints + "\nP2: " + cpuPoints)
                    .setCancelable(false)
                    .setPositiveButton("Novo Jogo", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialogInterface, int i) {
                            Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                            startActivity(intent);
                            finish();
                        }
                    })
                    .setNegativeButton("Sair", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialogInterface, int i) {
                            finish();
                        }
                    });
            AlertDialog alertDialog = alertDialogBuilder.create();
            alertDialog.show();
*
*
*
* */
