package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class AlterarConfiguracoes extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alterar_configuracoes);
    }

    public void ConfirmarAlteracoes(View view){
        Intent it = new Intent(AlterarConfiguracoes.this, Bem_Vindo_2.class);
        startActivity(it);
    }
}
