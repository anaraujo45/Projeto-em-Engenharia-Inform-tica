package com.example.asus.aprendecomigovelhinho

import android.content.ClipData
import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.BaseAdapter
import android.widget.TextView
import android.widget.Toast
import com.google.gson.GsonBuilder
import com.google.gson.JsonSyntaxException
import kotlinx.android.synthetic.main.activity_d_lista.*
import okhttp3.*
import java.io.IOException
import java.text.FieldPosition

class D_lista : AppCompatActivity() {

    //http://localhost:8080/caixaEntradaIdoso

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_d_lista)

        recyclerView_lista.layoutManager = LinearLayoutManager(this)
        //recyclerView_lista.adapter=MainAdapter()

        fetchJson()

    }

    fun fetchJson() {
        val url = "http://192.168.1.8:8080/caixaVariavel"

        val request = Request.Builder().url(url).build()

        val client = OkHttpClient()
        client.newCall(request).enqueue(object : Callback {
            override fun onResponse(call: Call?, response: Response?) {
                val body = response?.body()?.string()
                println(body)

                val gson = GsonBuilder().create()

                val homeFeed = gson.fromJson(body, HomeFeed::class.java)


                //json em string e a classe que representa o json
                runOnUiThread {

                    recyclerView_lista.adapter = MainAdapter(homeFeed)
                }

            }

            override fun onFailure(call: Call?, e: IOException?) {
                println("Falha ao executar")
            }

        })

    }
}


class HomeFeed(val questoes: List<String>)
