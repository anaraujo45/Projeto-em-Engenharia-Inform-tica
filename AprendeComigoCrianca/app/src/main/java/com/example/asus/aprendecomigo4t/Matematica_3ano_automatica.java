package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Matematica_3ano_automatica extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_matematica_3ano_automatica);
    }

    public void OpcaoMatematicaN3a (View view){
        Intent it = new Intent(Matematica_3ano_automatica.this,Matematica_3ano_na_automatica.class);
        startActivity(it);
    }
}
