package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Matematica_2ano_na_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_matematica_2ano_na_automatica);
    }


    public void OpcaoMatematica3a(View view){
        Intent it = new Intent(Matematica_2ano_na_automatica.this,Matematica_3ano_automatica.class);
        startActivity(it);
    }
}
