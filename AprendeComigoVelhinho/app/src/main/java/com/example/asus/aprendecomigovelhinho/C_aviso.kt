package com.example.asus.aprendecomigovelhinho

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class C_aviso : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_c_aviso)
    }


    fun c_avancar_d(view: View) {
        val it = Intent(this, D_lista::class.java)
        startActivity(it)

    }
}
