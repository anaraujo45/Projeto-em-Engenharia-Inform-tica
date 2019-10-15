package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Portugues_2ano_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_portugues_2ano_automatica);
    }

    public void OpcaoPortugues2a(View view){
        Intent it = new Intent(Portugues_2ano_automatica.this, Portugues_2ano_na_automatica.class);
        startActivity(it);
    }
}
