package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Matematica_1ano_na_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_matematica_1ano_na_automatica);
    }

    public void OpcaoMatematica2a(View view){
        Intent it = new Intent(Matematica_1ano_na_automatica.this,Matematica_2ano_automatica.class);
        startActivity(it);
    }
}
