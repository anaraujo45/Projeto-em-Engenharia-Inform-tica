package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_g_ex2_estmei.*
import kotlinx.android.synthetic.main.activity_g_ex3_estmei.*

class G_ex2Estmei : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_g_ex2_estmei)
    }

    fun g2_avancar_d(view: View) {
        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun corrigir(view: View){
        editTextPeleNua==null
        editTextPelo==null
        editTextCarapaca==null
        editTextEscamas==null
        editTextPenas==null

    }

    fun validar(view: View) {

        //ligar o serviço para dar resposta afirmativa, POST COM A CORRECAO

        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

}
