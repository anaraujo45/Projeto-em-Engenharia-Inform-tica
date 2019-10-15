package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Portugues_3ano_na_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_portugues_3ano_na_automatica);
    }


    public void OpcaoPortugues3Na(View view){
        Intent it = new Intent(Portugues_3ano_na_automatica.this, Portugues_4ano_automatica.class);
        startActivity(it);
    }
}
