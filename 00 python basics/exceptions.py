while True:
    try:
        number = int(input('Write your favorite number:'))
        print( 5 / number)
        break
    except ValueError:
        print('Make sure to enter a number')
    except ZeroDivisionError:
        print('Do not enter zero')
    except:
        print('This catches all other exceptions')
    finally:
        print('Loop ends here')
