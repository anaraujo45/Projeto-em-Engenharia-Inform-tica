package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.activity_d_lista.*
import kotlinx.android.synthetic.main.activity_e_ex2_port.*
import kotlinx.android.synthetic.main.activity_g_ex3_estmei.*
import okhttp3.*
import java.io.IOException

class E_ex2Port : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_e_ex2_port)

        fetchJson()

    }

    fun e2_avancar_d(view: View) {
        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun corrigir(view: View){
        editTextProverbio==null
    }

    fun validar(view: View) {

        //ligar o serviço para dar resposta afirmativa, POST COM A CORRECAO

        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun fetchJson(){
        val url = "http://****/portugues2/naoAutomatica/get"

        val request = Request.Builder().url(url).build()

        val client = OkHttpClient()
        client.newCall(request).enqueue(object: Callback {
            override fun onResponse(call: Call?, response: Response?) {
                val body = response?.body()?.string()
                println(body)

                val gson = GsonBuilder().create()


                //val ex2 = gson.fromJson(body, Proverbio::class.java)

                //json em string e a classe que representa o json
                runOnUiThread {
                    //ex2.toString()
                    editTextProverbio
                    editTextProverbio.text
                }

            }

            override fun onFailure(call: Call?, e: IOException?) {
                println("Falha ao executar")
            }

        })
    }
}

