package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Bem_Vindo_2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bem__vindo_2);
    }

    public void PlayMenu(View view){
        Intent it = new Intent(Bem_Vindo_2.this,Menu.class);
        startActivity(it);
    }

    public void AlterarConf(View view){
        Intent it = new Intent(Bem_Vindo_2.this,AlterarConfiguracoes.class);
        startActivity(it);
    }
}
