package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Portugues_4ano_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_portugues_4ano_automatica);
    }

    public void OpcaoPortugues4a(View view){
        Intent it = new Intent(Portugues_4ano_automatica.this, Portugues_4ano_na_automatica.class);
        startActivity(it);
    }
}
