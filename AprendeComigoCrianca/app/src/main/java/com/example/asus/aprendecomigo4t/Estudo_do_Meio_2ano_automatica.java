package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Estudo_do_Meio_2ano_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_estudo_do__meio_2ano_automatica);
    }

    public void OpcaoEDMN2a(View view){
        Intent it = new Intent(Estudo_do_Meio_2ano_automatica.this,Estudo_do_Meio_2ano_na_automatica.class);
        startActivity(it);
    }
}
