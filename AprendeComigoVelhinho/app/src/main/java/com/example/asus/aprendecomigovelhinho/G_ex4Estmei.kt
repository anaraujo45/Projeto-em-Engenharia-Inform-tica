package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_g_ex4_estmei.*

class G_ex4Estmei : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_g_ex4_estmei)
    }

    fun g4_avancar_d(view: View) {
        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun corrigir(view: View){
        editTextSerras==null
        editTextRios==null
    }

    fun validar(view: View) {

        //ligar o serviço para dar resposta afirmativa, POST COM A CORRECAO

        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }
}
