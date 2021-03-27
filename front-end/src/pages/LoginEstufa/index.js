import React, { useState } from 'react';
import { useForm } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import { Conteiner, A,  } from "./styles"
import Title from '../../components/Title'
import Button from '../../components/Button'
import schema from './validation'
import Form from '../../components/Form';
import Main from '../../components/Main';
import InputText from '../../components/Input/';
import Ola from '../../components/Ola'
import Modal from '../../components/Modal'


function LoginEstufa() {
 
    const [isModalVisible, setIsModalVisible] = useState(false);
    const { register, handleSubmit, errors } = useForm({
        resolver: yupResolver(schema)
    });
    const newUser = (user) => {
        console.log(user)
    };
   
        return (
            <Main>
               
                <Form onSubmit={handleSubmit(newUser)}>
                 
                       <Ola></Ola>
                        <Title title="Entre com sua conta" />
                   
                       
                    <InputText labelText="Nome" name="name" type="text" register={register}></InputText>
                    {errors.name?.message && <Modal onClose={() => setIsModalVisible(false)}
                    titulo="Erro"
                    conteudo={errors.name?.message} 
                    pagina="/cadastro"                 
                    /> }
                     
                  
                    <InputText labelText="Email" name="email" type="email" register={register} />
                    {errors.email?.message}
                   
                    <Button>Enviar</Button>
                    <Conteiner>
                        <A href="/cadastro"> Me cadastrar :) </A>
                        <A href="/recuperar" >Recuperar</A>
                    </Conteiner>
                </Form>
            </Main>
        )
        }

    
       




 
export default LoginEstufa;