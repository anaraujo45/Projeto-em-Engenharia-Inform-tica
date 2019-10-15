package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import com.google.gson.Gson
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.activity_d_lista.*
import kotlinx.android.synthetic.main.activity_f_ex3_mat.*
import kotlinx.android.synthetic.main.activity_g_ex3_estmei.*
import okhttp3.*
import okhttp3.Request
import java.io.IOException

class F_ex3Mat : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_f_ex3_mat)

        var editText: EditText? = null
        editText = findViewById<EditText>(R.id.editTextRespostaAviario)
        fetchJson()
    }

    fun f3_avancar_d(view: View) {
        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun corrigir(view: View){
        editTextRespostaAviario==null
    }

    fun validar(view: View) {

        val url = "http://192.168.1.8:8080/matematica3/naoAutomatica/post"

        data class NumeroGalinhasInfo(val resposta: String)
        data class NumeroGalinhasRequest(val numeroGalinhas: NumeroGalinhasInfo)
        val numeroGalinhasRequest = NumeroGalinhasRequest(numeroGalinhas = NumeroGalinhasInfo(resposta =  ""))

        val json = Gson().toJson(numeroGalinhasRequest)
        val body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), json)
        val request = Request.Builder().url(url).post(body).build()


        val it = Intent(this, D_lista::class.java)
        startActivity(it)
    }

    fun fetchJson(){

        val url = "http://192.168.1.8:8080/matematica3/naoAutomatica/get"

        val request = Request.Builder().url(url).build()

        val client = OkHttpClient()
        client.newCall(request).enqueue(object : Callback {

            override fun onResponse(call: Call?, response: Response?) {
                val body = response?.body()?.string()
                println(body)

                editTextRespostaAviario?.setText(body)
            }

            override fun onFailure(call: Call?, e: IOException?) {
                println("${e?.message}")
            }

        })
    }
}
