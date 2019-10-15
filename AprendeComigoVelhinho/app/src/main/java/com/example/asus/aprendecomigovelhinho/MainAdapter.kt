package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import java.text.SimpleDateFormat
import kotlinx.android.synthetic.main.activity_d_lista_row.view.*
import kotlinx.android.synthetic.main.activity_e_ex2_port.view.*
import android.R.attr.data
import java.util.*


class MainAdapter(val homeFeed: HomeFeed): RecyclerView.Adapter<CustomViewHolder>(){

    //val lista = listOf("Português 1º ano", "Português 2º ano", "Português 3º ano", "Português 4º ano")

    override fun getItemCount(): Int {
        return homeFeed.questoes.count()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {
        val layoutInflater = LayoutInflater.from(parent?.context)
        val cellForRow = layoutInflater.inflate(R.layout.activity_d_lista_row, parent, false)
        return CustomViewHolder(cellForRow, homeFeed)
    }

    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {
        //val listaquestoes = lista.get(position)
        //holder?.view?.textView_questao?.text=listaquestoes

        val caixa = homeFeed.questoes.get(position)
        holder?.view?.textView_questao?.text=caixa

        val formataData = SimpleDateFormat("dd-MM-yyyy - HH:mm")
        val data = Date()
        val dataFormatada = formataData.format(data)

        holder?.view?.textViewPosicao?.text="Data: $dataFormatada"

    }

}

class CustomViewHolder(val view: View, val homeFeed: HomeFeed): RecyclerView.ViewHolder(view){
    init {
        view.setOnClickListener{
            var disciplina=homeFeed.questoes.get(position)

            //Português
            if(disciplina.equals("Português 1º ano")) {
                val intent = Intent(view.context, E_ex1Port::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Português 2º ano")) {
                val intent = Intent(view.context, E_ex2Port::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Português 3º ano")) {
                val intent = Intent(view.context, E_ex3Port::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Português 4º ano")) {
                val intent = Intent(view.context, E_ex4Port::class.java)
                view.context.startActivity(intent)
            }

            //Matemática
            if(disciplina.equals("Matemática 1º ano")) {
                val intent = Intent(view.context, F_ex1Mat::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Matemática 2º ano")) {
                val intent = Intent(view.context, F_ex2Mat::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Matemática 3º ano")) {
                val intent = Intent(view.context, F_ex3Mat::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Matemática 4º ano")) {
                val intent = Intent(view.context, F_ex4Mat::class.java)
                view.context.startActivity(intent)
            }

            //Estudo do Meio
            if(disciplina.equals("Estudo do Meio 1º ano")) {
                val intent = Intent(view.context, G_ex1Estmei::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Estudo do Meio 2º ano")) {
                val intent = Intent(view.context, G_ex2Estmei::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Estudo do Meio 3º ano")) {
                val intent = Intent(view.context, G_ex3Estmei::class.java)
                view.context.startActivity(intent)
            }
            if(disciplina.equals("Estudo do Meio 4º ano")) {
                val intent = Intent(view.context, G_ex4Estmei::class.java)
                view.context.startActivity(intent)
            }
        }
    }
}

