<template>
    <div class="card-container">
        <el-card class="box-card">
            <h3>修改brand</h3>
            <y-form
                    ref="brandForm"
                    :model="brandForm"
                    :rules="brandRules"
                    label-width="100px"
            >
                <el-row>
                    
                    <el-col :span="12">
                        <el-form-item label="品牌名称:" prop="brand">



                            
                            
                                <y-input
                            
                            v-model="brandForm.brand"
                            
                            
                            
                            
                            
                            
                            
                            
                            />


                        </el-form-item>
                    </el-col>
                    

                    <el-col :span="24">
                        <el-form-item>
                            <el-button @click="submit('brandForm')">提交</el-button>
                            <el-button @click="back">返回</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </y-form>
        </el-card>
    </div>
</template>

<script>

    import { putBrand, getBrand } from "@/api/brand"


    
    
    
    

    export default {

        data() {
            return {
                brandForm: {},
                brandRules: {
                
                
                
                
            },

                
                    
                        
                
        }
        },
        created() {
            this.getBrand()
        },
        methods: {
            async getBrand() {
                const res = await getBrand(this.$route.query.id)
                this.brandForm = res.data
            },

            async putBrand() {
                await putBrand(this.$route.query.id, this.brandForm)
                this.$router.push({ path: "/brand" })

                this.$message({
                    message: "修改成功",
                    type: "success"
                })
            },

            async submit() {
                this.$refs.brandForm.check((valid) => {
                    if (valid) {
                        this.putBrand()
                    } else {
                        return false
                    }
                })
            }

        }

    }
</script>
<style lang='scss' scope>
    .card-container {
        background-color: #f0f2f5;
        padding: 30px;
        min-height: 100vh;

        .box-card {

        }
    }
</style>